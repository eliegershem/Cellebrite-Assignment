pipeline {
    agent any
    
    environment {
        DOCKER_CREDS = credentials('DockerCred')
    }

    }
    stages {

        stage("build") {

            steps{
                sh 'docker build -t cellebrite-morse ./Image/'
            }
        }

        stage("push") {

            steps{
                sh 'docker build -t cellebrite-morse ./Image/'
            }
        }

    }
}