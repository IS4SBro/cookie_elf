from numpy.random import randint

COOKIES: list[str] = [
    "Georges Melies",
    "Georges Melies",
    "Georges Melies",
    "Georges Melies",
    "James Clerk Maxwell",
    "James Clerk Maxwell",
    "James Clerk Maxwell",
    "Mary Antoinette",
    "Mark Twain",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Clives Staples Lewis",
    "Lego Man #7",
    "Lego Man #3",
]


class CookieElf:
    def om_nom_eat_them_cookies(self, cookies: list[str]) -> None:
        self.cookies: list[str] = cookies
        self.plebians: dict[str, int] = dict({plebian : self.cookies.count(plebian) for plebian in set(cookies)})
        self.plebians = dict(sorted(self.plebians.items()))  # sort the dict by those with the most cookies

    def dictate(self) -> dict[str, list[str]]:
        decree: dict[str, list[str]] = {}
        for plebian in self.plebians.keys():
            other_plebians = [other_plebian for other_plebian in self.cookies if other_plebian != plebian]
            n_cookies = self.plebians[plebian]  # len(["Eateth not the cookies, or they will eateth your belt." for c in self.cookies if c == plebian])
            for cookie in range(n_cookies):
                decreed_plebian = other_plebians.pop(0 if len(other_plebians) == 1 else randint(0, len(other_plebians) - 1))
                the_plebians_assignments = decree.get(plebian, [])
                the_plebians_assignments.append(decreed_plebian)
                decree[plebian] = the_plebians_assignments
                self.cookies.remove(decreed_plebian)
        return decree
    
if __name__ == "__main__":
    the_elf = CookieElf()
    the_elf.om_nom_eat_them_cookies(COOKIES)
    decree = the_elf.dictate()
    print("🎄 Thus sayeth the master elf! Hear ye! Hear YE! 🎄")
    for plebian, cookies in decree.items():
        print(f"Unto {plebian} is assigned the following:")
        for cookie in cookies:
            print(f" - {cookie}")
    print("This concludes my proclaimation. May the snow fall gently on your visiage ❄️")