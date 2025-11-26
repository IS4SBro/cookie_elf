from numpy.random import randint

COOKIES: list[str] = [
    "JoeBob",
    "Jean",
    "Bart",
    "Cinderella",
    "Hawthorne",
    "Leonardo",
    "Adeline",
    "Mateo",
    "Leonardo",
    "Adeline",
    "Mateo",
    "Kline",
    "Lauren",
    "William",
    "Bambi",
    "Richard",
    "Wendell",
    "Wendell",
    "Wendell",
    "Lennorde",
    "Lennorde",
    "Lennorde",
    "Rocky",
    "Rocky",
    "Rocky",
]
BOGARTS = ["JoeBob", "Jean", "Bart", "Cinderella", "Hawthorne"]
IRIDRIANS = ["Leonardo", "Adeline", "Mateo"]
AXLWAXERS = ["Kline", "Lauren", "William", "Bambi", "Richard"]
ROBERTSON = ["Wendell"]
SMITH = ["Rocky"]
ANTIOC = ["Lennorde"]

COOKIE_GROUPS = [BOGARTS, IRIDRIANS, AXLWAXERS, ROBERTSON, SMITH, ANTIOC]
COOKIE_GROUP_MAP = {
    p: g for p in set(COOKIES.copy()) for g in COOKIE_GROUPS.copy() if p in g
}


class CookieElf:
    def om_nom_eat_them_cookies(self, cookies: list[str]) -> None:
        self.cookies: list[str] = cookies
        self.plebians: dict[str, int] = dict(
            {plebian: self.cookies.count(plebian) for plebian in set(cookies)}
        )
        self.plebians = dict(
            sorted(self.plebians.items())
        )  # sort the dict by those with the most cookies

    def dictate(self) -> dict[str, list[str]]:
        decree: dict[str, list[str]] = {}
        for plebian in self.plebians.keys():
            other_plebians = [
                other_plebian
                for other_plebian in self.cookies
                if other_plebian != plebian
            ]
            n_cookies = self.plebians[
                plebian
            ]  # len(["Eateth not the cookies, or they will eateth your belt." for c in self.cookies if c == plebian])
            for cookie in range(n_cookies):
                if not other_plebians:
                    return decree  # Return faulty decree
                decreed_plebian = other_plebians.pop(
                    0
                    if len(other_plebians) == 1
                    else randint(0, len(other_plebians) - 1)
                )
                the_plebians_assignments = decree.get(plebian, [])
                the_plebians_assignments.append(decreed_plebian)
                decree[plebian] = the_plebians_assignments
                self.cookies.remove(decreed_plebian)
        return decree


def print_decree(decree: dict[str, list[str]]) -> None:
    for plebian, cookies in decree.items():
        print(f"Unto {plebian} is assigned the following:")
        for cookie in cookies:
            print(f" - {cookie}")


def run_by_the_master_master_elf(
    decree: dict[str, list[str]], verbose=True
) -> bool:
    try:
        all_plebs = set(COOKIES)
        decreed_plebs = set(decree.keys())
        assert not all_plebs.difference(
            decreed_plebs
        ), f"Not all plebians have an assignment ({all_plebs.difference(decreed_plebs)})👎"

        for pleb, cookies in decree.items():
            assert (
                pleb not in cookies
            ), f"{pleb} cannot give themselves a cookie 👎"
            n_cookies = COOKIES.count(pleb)
            n_given = len(decree[pleb])
            assert (
                n_given == n_cookies
            ), f"{pleb} needs to give {n_cookies} cookies 👎"
            n_received = sum([c.count(pleb) for c in decree.values()])
            assert (
                n_received == n_cookies
            ), f"{pleb} needs to receive {n_cookies} cookies 👎"
            assert len(set(cookies)) == len(
                cookies
            ), f"{pleb} is giving multiple cookies to the same person 👎"
            cookie_group = COOKIE_GROUP_MAP.copy()[pleb]
            assert not set(cookie_group).intersection(
                cookies
            ), f"{pleb} cannot be giving cookies to other plebs in the same family unit 👎"

    except AssertionError as e:
        if verbose:
            print("Master-Master Elf says: " + e.args[-1])
            print(f"This is a faulty decree:")
            print_decree(decree)
        return False
    if verbose:
        print("Master-Master Elf says ✅")
    return True


if __name__ == "__main__":
    the_elf = CookieElf()
    the_elf.om_nom_eat_them_cookies(COOKIES.copy())
    decree = the_elf.dictate()
    while not run_by_the_master_master_elf(decree, verbose=False):
        the_elf.om_nom_eat_them_cookies(COOKIES.copy())
        decree = the_elf.dictate()
    print("🎄 Thus sayeth the master elf! Hear ye! Hear YE! 🎄")
    print_decree(decree)
    print(
        "This concludes my proclaimation. May the snow fall gently on your visiage ❄️"
    )
