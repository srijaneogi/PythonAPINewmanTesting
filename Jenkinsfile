pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python demo2.py -coll_run Titan.postman_collection.json'
            }
        }
    }
}
