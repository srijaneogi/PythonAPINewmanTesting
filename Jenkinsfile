pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'whoami'
                sh 'python3 demo2.py -coll_run Titan.postman_collection.json'
            }
        }
    }
}
