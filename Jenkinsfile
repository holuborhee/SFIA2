pipeline {
    agent any 
    stages {
        stage('Build Dependencies') { 
            steps {
                sh 'chmod +x ./scripts/*'
                sh './scripts/dependencies.sh'
                sh './scripts/ansible.sh'
            }
        }
        stage('Deploy') { 
            steps {
                sh 'sudo docker-compose build'
                sh 'sudo docker login'
                sh 'sudo docker push ngww/service1:latest'
                sh 'sudo docker push ngww/service2:latest'
                sh 'sudo docker push ngww/service3:latest'
                sh 'sudo docker push ngww/service4:latest'
                sh 'sudo docker stack deploy --compose-file docker-compose.yaml sfia2' 
            }
        }
    }
}