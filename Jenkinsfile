pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git' https://github.com/varshalahane2004-ops/main-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cicd-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 cicd-app'
            }
        }
    }
}