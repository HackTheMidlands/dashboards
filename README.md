# Announcement Dashboard

Excuse the whole thing really.

## Structure

- Flask to act as an input form
- InfluxDB to store timestamped *events*
- Grafana to present the data

## Further considerations

- Since Grafana is probably not the best idea for longer texts, if information is being posted anywhere else a link to this can be embedded.
- Flask **Needs** Some authentication. But additionally we could just firewall it in.
    - This is rather dependant on how we want to display this.
    - Would it be acceptable to just segment the network it runs on.
- InfluxDB currently is very open but it isn't exposed to anything other than ```Flask``` and ```Grafana``` across the internal docker network.