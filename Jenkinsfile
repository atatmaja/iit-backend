pipeline {
  agent { 
    docker { 
      image 'python:3.7.2' 
      args '''
        -e PATH="$PATH:/var/lib/jenkins/jobs/iit-backend/branches/ci-integration/workspace/.local/bin"
      '''
      // TODO: Fix the above environment variable to not depend on a branch
    } 
  }
  environment {
    FLASK_ENV = 'prod'
    AIRTABLE_API_KEY = credentials('airtable_api_key')
    AIRTABLE_BASE_ID = credentials('airtable_base_id')
  } 
  stages {
    stage('Build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install -r requirements.txt --user'
          sh 'python manage.py'
        }
      }
    }
  }
}

