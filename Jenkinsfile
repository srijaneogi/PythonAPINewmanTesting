pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                
                sh 'python3 demo2.py -coll_run Titan.postman_collection.json'
            }
        }

    
    stage('wait') {
                    steps {
                        script {
                            timeout(2) {
                                def folder = new File( '${WORKSPACE}/newman' )
                                println "Waiting for " + folder
                                println "folder==" + folder.exists()
                                waitUntil {
					def exitCode = sh script: 'find . -name newman | egrep .', returnStatus: true
                                        exitCode == 0                                    
                                }
                            }
                        }
                    }
                }
    }
    post {
        always {
                archiveArtifacts artifacts: 'newman/*.html'
		publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'newman', reportFiles: '*.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])
        }
    }
}
