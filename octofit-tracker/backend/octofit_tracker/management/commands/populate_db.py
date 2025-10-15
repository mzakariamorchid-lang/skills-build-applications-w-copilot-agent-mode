from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', username='Iron Man', team=marvel, is_superhero=True),
            User(email='spiderman@marvel.com', username='Spider-Man', team=marvel, is_superhero=True),
            User(email='captain@marvel.com', username='Captain America', team=marvel, is_superhero=True),
            User(email='batman@dc.com', username='Batman', team=dc, is_superhero=True),
            User(email='superman@dc.com', username='Superman', team=dc, is_superhero=True),
            User(email='wonderwoman@dc.com', username='Wonder Woman', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Workouts
        workouts = [
            Workout(name='Cardio Blast', description='High intensity cardio', difficulty='Medium'),
            Workout(name='Strength Training', description='Build muscle', difficulty='Hard'),
            Workout(name='Yoga Flow', description='Flexibility and balance', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)

        # Activities
        ironman = User.objects.get(username='Iron Man')
        batman = User.objects.get(username='Batman')
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=batman, type='Cycling', duration=45)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
