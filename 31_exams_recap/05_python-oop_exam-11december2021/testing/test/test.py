from unittest import TestCase, main

from project.team import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team("SomeTeam")

    def test_initialization_correct(self):
        self.assertEqual("SomeTeam", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_wrong_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "SomeTeam1"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_correct(self):
        actual = self.team.add_member(Ivan=24, Petkan=36)
        expected = f'Successfully added: Ivan, Petkan'
        self.assertEqual(expected, actual)
        self.assertEqual({'Ivan': 24, 'Petkan': 36}, self.team.members)

    def test_add_member_with_existing_member(self):
        self.team.add_member(Ivan=24, Petkan=36)
        expected = f'Successfully added: '
        actual = self.team.add_member(Ivan=38)
        self.assertEqual(expected, actual)
        self.assertEqual({'Ivan': 24, 'Petkan': 36}, self.team.members)

    def test_remove_member_correct(self):
        self.team.add_member(Ivan=24, Petkan=36)
        expected = f"Member Ivan removed"
        actual = self.team.remove_member("Ivan")
        self.assertEqual(expected, actual)
        self.assertEqual({'Petkan': 36}, self.team.members)

    def test_remove_member_non_existing_member(self):
        self.team.add_member(Ivan=24, Petkan=36)
        expected = f"Member with name Georgi does not exist"
        actual = self.team.remove_member("Georgi")
        self.assertEqual(expected, actual)
        self.assertEqual({'Ivan': 24, 'Petkan': 36}, self.team.members)

    def test__gt__(self):
        self.team.add_member(Ivan=24, Petkan=36)
        self.team2 = Team("OtherTeam")
        self.team2.add_member(Ivan=24)
        self.assertEqual(True, self.team.__gt__(self.team2))
        self.assertEqual(False, self.team2.__gt__(self.team))

    def test__len__(self):
        self.team.add_member(Ivan=24, Petkan=36)
        self.assertEqual(2, self.team.__len__())

    def test__add__(self):
        self.team.add_member(Ivan=24, Petkan=36)
        self.team2 = Team("OtherTeam")
        self.team2.add_member(Georgi=27)
        self.team3 = self.team.__add__(self.team2)
        expected = self.team3
        self.assertEqual(expected, self.team3)
        self.assertEqual("SomeTeamOtherTeam", self.team3.name)
        self.assertEqual(3, self.team3.__len__())

    def test__str__(self):
        self.team.add_member(Ivan=24, Petkan=36)
        expected = f'Team name: SomeTeam\n' \
                   f'Member: Petkan - 36-years old\n' \
                   f'Member: Ivan - 24-years old'
        self.assertEqual(expected, self.team.__str__())


if __name__ == "__main__":
    main()
