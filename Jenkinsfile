pipeline {
    agent any 
    stages {
        stage('Build Dependencies') { 
            steps {
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