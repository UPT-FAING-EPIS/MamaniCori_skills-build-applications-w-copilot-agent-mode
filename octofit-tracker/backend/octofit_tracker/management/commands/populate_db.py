from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', username='IronMan', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', username='CaptainAmerica', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        squats = Workout.objects.create(name='Squats', description='Legs', difficulty='Easy')

        # Activities
        Activity.objects.create(user=ironman, workout=pushups, duration=30, calories_burned=200)
        Activity.objects.create(user=captain, workout=running, duration=45, calories_burned=400)
        Activity.objects.create(user=batman, workout=squats, duration=20, calories_burned=150)
        Activity.objects.create(user=superman, workout=running, duration=60, calories_burned=600)

        # Leaderboard
        Leaderboard.objects.create(user=ironman, score=500, rank=2)
        Leaderboard.objects.create(user=captain, score=600, rank=1)
        Leaderboard.objects.create(user=batman, score=300, rank=4)
        Leaderboard.objects.create(user=superman, score=400, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
