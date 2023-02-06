pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python demo.py -coll_run Titan.postman_collection.json'
            }
        }
    }
}
