from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/jobs", methods=["POST"])
def search_jobs():
  # Get the uploaded transcripts and resume
  transcripts = request.files["transcripts"]
  resume = request.files["resume"]

  # Send a request to LinkedIn, Glassdoor, and Indeed with the transcripts and resume
  # and retrieve the search results
  linkedin_results = requests.post("https://linkedin.com/jobs/search", data={"transcripts": transcripts, "resume": resume})
  glassdoor_results = requests.post("https://glassdoor.com/jobs/search", data={"transcripts": transcripts, "resume": resume})
  indeed_results = requests.post("https://indeed.com/jobs/search", data={"transcripts": transcripts, "resume": resume})

  # Combine the results from all three job search websites and return them to the client
  results = linkedin_results + glassdoor_results + indeed_results
  return results

@app.route("/courses", methods=["POST"])
def suggest_courses():
  # Get the entered dream job and resume
  dream_job = request.form["dream-job"]
  resume = request.files["resume"]

  # Send a request to a course suggestion API with the dream job and resume
  # and retrieve the suggested courses
  courses = requests.post("https://courses.com/suggest", data={"dream_job": dream_job, "resume": resume})

  # Return the suggested courses to the client
  return courses

if __name__ == "__main__":
  app.run()
