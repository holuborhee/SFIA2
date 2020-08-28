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
                sh 'sudo docker stack deploy --compose-file docker-compose.yaml sfia2' 
            }
        }
    }
}