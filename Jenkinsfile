pipeline {
    agent any 
    stages {
        stage('Get Repo') {
            steps {
                sh 'chmod +x ./scripts/*'
                sh './scripts/getrepo.sh'
            }
        }
        stage('Build Dependencies') { 
            steps {
                sh 'chmod +x ./scripts/*'
                sh './scripts/dependencies.sh'
                sh './scripts/ansible.sh'
            }
        }
        stage('Test application') {
            steps {
                sh 'chmod +x ./scripts/*'
                sh './scripts/tests.sh'
            }
        }
        stage('Deploy') { 
            steps {
                sh 'source /home/jenkins/.profile'
                sh 'sudo chmod 666 /var/run/docker.sock'
                sh 'docker-compose build'
                sh 'sudo docker login'
                sh 'sudo docker push ngww/service1:latest'
                sh 'sudo docker push ngww/service2:latest'
                sh 'sudo docker push ngww/service3:latest'
                sh 'sudo docker push ngww/service4:latest'
                sh 'docker stack deploy --compose-file docker-compose.yaml sfia2'
            }
        }
    }
}
