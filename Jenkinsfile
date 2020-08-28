pipeline {
    agent any 
    stages {
        stage('Get Repo') {
            steps {
                sh './scripts/getrepo.sh'
            }
        }
        stage('Build Dependencies') { 
            steps {
                sh 'chmod +x ./scripts/*'
                sh './scripts/dependencies.sh'
                sh './scripts/ansible.sh'
                sh 'ansible-playbook -i inventory.cfg playbook.yaml'
            }
        }
        stage('Deploy') { 
            steps {
                sh './scripts/deploy.sh' 
            }
        }
    }
}