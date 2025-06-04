#!/usr/bin/python3

from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(5, 90)

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task()
    def hello_world(self):
        self.client.get("/")
        self.client.get("/status")



