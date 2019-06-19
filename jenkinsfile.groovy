node any {
    stage('Build') {
        bat label: '', script: ' docker build -f ./Dockerfile . -t skruvi/worldofgames:latest'
    }
}