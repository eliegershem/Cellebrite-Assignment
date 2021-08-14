pipeline {
    agent any
    
    environment {
        DOCKER_CREDS = credentials('DockerCred')
    }

    stages {
         stage("change port main") {
            when {
                branch 'main'
            } 
            steps{
                sh 'sed -i \'s/8000/4000/g\' ./Image/Dockerfile'
            }
        }

        stage("change port develop") {
            when {
                branch 'main'
            } 
            steps{
                sh 'sed -i \'s/8000/5000/g\' ./Image/Dockerfile'
            }
        }


        stage("build") {

            steps{
                sh 'sudo docker build -t eliegershem/cellebrite-morse ./Image/'
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