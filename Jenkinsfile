pipeline {
    agent {
        docker {
            image 'my-jenkins'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Maxxksim/sysprog-os-admin-labs.git'
            }
        }
        stage('Download DEB package') {
            steps {
                sh '''
                    curl -L https://github.com/Maxxksim/sysprog-os-admin-labs/raw/main/packages/counter-1.0-2.deb -o /tmp/counter-1.0-2.deb
                '''
            }
        }
        stage('Install DEB') {
            steps {
                sh '''
                    sudo dpkg -i /tmp/counter-1.0-2.deb
                '''
            }
        }
        stage('Download script') {
            steps {
                sh '''
                    curl -L https://github.com/Maxxksim/sysprog-os-admin-labs/raw/main/scripts/counter.sh -o /tmp/counter.sh
                    chmod +x /tmp/counter.sh
                '''
            }
        }
        stage('Run script') {
            steps {
                sh '/tmp/counter.sh'
            }
        }
    }
}
