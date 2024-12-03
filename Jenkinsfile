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
                    curl -L https://github.com/Maxxksim/sysprog-os-admin-labs/raw/main/deb-package.deb -o deb-packgae.deb
                '''
            }
        }
        stage('Install DEB') {
            steps {
                sh '''
                    sudo dpkg -i deb-packgae.deb
                '''
            }
        }
        stage('Download script') {
            steps {
                sh '''
                    curl -L https://github.com/Maxxksim/sysprog-os-admin-labs/raw/main/counter.sh -o counter.sh
                    chmod +x counter.sh
                    sudo mv counter.sh /usr/local/bin/counter
                '''
            }
        }
        stage('Run script') {
            steps {
                sh 'counter.sh'
            }
        }
    }
}
