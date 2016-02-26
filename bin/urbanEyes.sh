
# Script Demonio UrbanEyes
#! /bin/sh


ruta=/home/pi/Documents/urbaneyes                       #Home del Programa
startup=$ruta/bin/startup.sh                            #Startup
shutdown=$ruta/bin/shutdown.sh                          #Shutdown

echo "corriendo Demonio"

estado="holaa"

start(){
        echo "sensoresFinal.py"
        $startup
        echo $estado
}

stop(){
        $shutdown
        echo "me estas matando"
}
case "$1" in
        start)
                start
                ;;
        stop)
                stop
                ;;
        *)
        echo $"Usar: $0 {start|stop} "
        # exit 1
esac
# el codigo exit 0 ejecita un exit en la consola
# exit 0



