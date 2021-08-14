pipeline {
    agent any
    
    environment {
        DOCKER_CREDS = credentials('DockerCred')
    }

    stages {

        stage("build") {

            steps{
                sh 'whoami'
                sh 'sudo docker build -t eliegershem/cellebrite-morse ./Image/'
            }
        }

        stage("change port") {

            steps{
                sh 'echo this is running'
            }
        }

        stage("push") {

            steps{
                sh 'echo $DOCKER_CREDS_PSW | sudo docker login -u $DOCKER_CREDS_USR --password-stdin'
                sh 'sudo docker push eliegershem/cellebrite-morse:latest'
            }
        }

    }
}