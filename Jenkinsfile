pipeline {
    agent any 
    stages {
        stage('Build Dependencies') { 
            steps {
                sh 'chmod +x ./scripts/*'
                sh './script/dependencies.sh'
                sh './script/ansible.sh'
            }
        }
        stage('Deploy') { 
            steps {
                sh './script/deploy.sh' 
            }
        }
    }
}