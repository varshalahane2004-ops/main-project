pipeline {
    agent any

    stages {

        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t cicd-app .'
            }
        }

        stage('Stop Old Container (if any)') {
            steps {
                bat '''
                docker stop cicd-app-container || exit 0
                docker rm cicd-app-container || exit 0
                '''
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d --name cicd-app-container -p 5000:5000 cicd-app'
            }
        }
    }
}