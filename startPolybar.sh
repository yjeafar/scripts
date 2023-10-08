# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use
# polybar-msg cmd quit

# Set environemnt variable for all monitors which is used in config to start on polybar on each monitor

# Launch Polybar, using default config location ~/.config/polybar/config.ini
# Loop is to detect monitor connections and show polybar on each one using env variable that is set in loop
if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    # MONITOR=$m polybar --reload main &
    MONITOR=$m bash ~/.config/polybar/launch.sh --grayblocks  2>&1 | tee -a /tmp/polybar.log & disown 
  done
else
  polybar --reload main &
fi

bash ~/scripts/hidePolybarTaskbar.sh

spotify-listener 
& disown
echo "Polybar launched..."
