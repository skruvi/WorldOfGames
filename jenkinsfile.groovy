node any {
    cleanWs()
    stage('Build') {
        sh 'docker build -f ./Dockerfile . -t skruvi/worldofgames:latest'
    }
}
