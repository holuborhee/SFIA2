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
                sh 'chmod +x ./scripts/*'
                sh './scripts/deploy.sh'
            }
        }
    }
}
