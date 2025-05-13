from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A')
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='activity@example.com', name='Activity User', password='pass')
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-05-13T00:00:00Z')
        self.assertEqual(activity.type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='workout@example.com', name='Workout User', password='pass')
        workout = Workout.objects.create(user=user, name='Pushups', description='Do 20 pushups', date='2025-05-13T00:00:00Z')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaderboard Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
