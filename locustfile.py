from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
	def on_start(self):
		r = self.client.get('/login/')
		self.client.post('/login/?next=/index', 
				{'username': 'test_user', 'password': 'test'}, headers={'X-CSRFToken': r.cookies['csrftoken']})    

	@task(1)
	def index(self):
		self.client.get("/index")

	@task(2)
	def profile(self):
		self.client.get("/profile")

class WebsiteUser(HttpLocust):
	task_set = UserBehavior
	min_wait = 5000
	max_wait = 9000

