node any {
    cleanWs()
    stage('Build') {
        sh label: '', script: 'docker build -f ./Dockerfile . -t skruvi/worldofgames:latest'
    }
}