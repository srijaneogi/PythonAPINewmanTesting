pipeline {
    agent { docker { image 'mudaliar20/python:v1' } }
    stages {
        stage('build') {
            steps {
                sh 'python demo2.py -coll_run Titan.postman_collection.json'
            }
        }
    }
}
