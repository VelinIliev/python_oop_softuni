from project.team import Team
import unittest


class TeamTests(unittest.TestCase):
    def setUp(self) -> None:
        self.team = Team("Levski")

    def test_initialisation(self):
        self.assertEqual("Levski", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            new_team = Team("CSKA1948")
        expected = f'Team Name can contain only letters!'
        self.assertEqual(expected, str(ve.exception))

    def test_add_members_correct(self):
        expected = "Successfully added: Ivan, Petkan"
        actual = self.team.add_member(Ivan=25, Petkan=21)
        self.assertEqual(expected, actual)

    def test_remove_member(self):
        self.team.add_member(Ivan=25, Petkan=21)
        expected = "Member Ivan removed"
        actual = self.team.remove_member("Ivan")
        self.assertEqual(expected, actual)
        self.assertEqual({'Petkan': 21}, self.team.members)

    def test_remove_member_non_existing(self):
        self.team.add_member(Ivan=25, Petkan=21)
        expected = 'Member with name Gosho does not exist'
        actual = self.team.remove_member("Gosho")
        self.assertEqual(expected, actual)
        self.assertEqual({'Ivan': 25, 'Petkan': 21}, self.team.members)

    def test_gt(self):
        self.team.add_member(Ivan=25, Petkan=21)
        team2 = Team("CSKA")
        team2.add_member(Ivan=25)
        self.assertEqual(True, self.team.__gt__(team2))
        self.assertEqual(False, team2.__gt__(team2))

    def test_len(self):
        self.team.add_member(Ivan=25, Petkan=21)
        self.assertEqual(2, self.team.__len__())

    def test_add(self):
        self.team.add_member(Ivan=25, Petkan=21)
        new_team = Team("Spartak")
        new_team.add_member(Gosho=25)
        added_team = self.team.__add__(new_team)
        self.assertEqual('LevskiSpartak', added_team.name)
        self.assertEqual({'Ivan': 25, 'Petkan': 21, 'Gosho': 25}, added_team.members)

    def test_str(self):
        self.team.add_member(Ivan=25, Petkan=21)
        expected = "Team name: Levski\n" \
                   "Member: Ivan - 25-years old\n" \
                   "Member: Petkan - 21-years old"
        actual = self.team.__str__()
        self.assertEqual(expected, actual)