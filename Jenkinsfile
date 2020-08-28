pipeline {
    agent any 
    stages {
        stage('Build Dependencies') { 
            steps {
                sh 'sudo apt update && sudo apt install -y python3 python3-pip'
                sh 'chmod +x ./scripts/*'
                sh './scripts/ansible.sh'
            }
        }
        stage('Deploy') { 
            steps {
                sh './scripts/deploy.sh' 
            }
        }
    }
}