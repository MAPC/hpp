# Housing Production Plan (HPP) Tool

HPP has two modes: server and headless. The server mode is what is deployed to https://hpp.mapc.org, while the headless mode is intended to be used by other programs that require HPP data.

Between the two input methods (server, headless), the program is split up into three components:
- **Datasets**: Describes how/what to fetch from the database and what operations to perform on the data once it has been retrieved. These datasets are constructed and orchestrated together by a DataComposer.
- **DataComposers**: Manages the lifecycles of any declared Datasets and provides hooks into the datasets for the Writers to use.
- **Writers**: Consumes a DataComposer and writes the DataComposer's contents to a file.

#### Headless Usage
`hpp -h [-m] [-f format] [-t tables] [-o outpath] municipalities`
##### Examples
```sh
# All tables for Boston, Somerville, and Cambridge, output as .csv files
hpp --headless -f csv "Boston, Somerville, Cambridge"

# Two tables, including metadata for each table, for Acton, output as an .xlsx file
hpp -h -f e --include-metadata --tables="Gross Rent, Race and Ethnicity Estimates" Acton

# All tables for Acton and Boston, saving to the desktop as the default file format
hpp -h -o /home/$(whoami)/Desktop "Acton, Boston"
```
##### Arguments
_-\-headless, -h_ : Start the HPP tool in headless mode. All other arguments require this flag.

_-\-include-metadata, -m_ : Includes metadata tables in output.

_-\-format, -f_ : The format of the output file. Possible options: c, csv, e, excel.

_-\-tables, -t_ : A comma-separated string argument containing the titles of the Datasets you want to process.

_-\-outpath, -o_ : An absolute path for where the output of the program should be written. The default path for headless mode is the current directory that the user is executing the command from.

_-\-latest_year_ : Will only grab data for the most recent year listed in each dataset.

> __Note:__ Any of these arguments can be passed to the `hpp` command via environment variables prefixed with `ARGS_` (e.g. `ARGS_HEADLESS=true`). This is vitally important if you choose to use Docker as your development environment.

### Configuration and Environment
All config options are listed in all-capped strings in _config/config.py_.
Create a _.env_ file in the project root and assign a PrQL token to `PRQL_TOKEN` and a port to `WEB_PORT` in the _.env_ (shared on Dashlane).

> __Note:__ It is not recommended to change the default configurations in the _config/defaults.py_ file when you
are customizing the execution for you environment. That file is in there to ensure that
the app is usable with little configuration. If you want to override the default configuration,
you should override the environment variables with a _.env_ file.

### Running the App
##### Using Python 3.x
```sh
# In project root
mkdir src/web/compositions
pip3 install -e .
hpp
```

The web server will not tell you where it is running, but it is accessible at 127.0.0.1:8081 by default.

##### With Docker + docker-compose
```sh
# In local repo project root
docker-compose up
```

### Deploying / Updating
The current deployment of the [HPP website](https://hpp.mapc.org) uses Docker for the runtime environment.

Once your SSH keys have been added to both your user and the HPP user on our production server, SSH into live and navigate to the project root on the server:
```sh
ssh youruser@live.mapc.org
cd /var/www/hpp
```

Run the commands to deploy from the Docker container:
```sh
sudo git pull \
&& sudo docker-compose up -d --no-deps --build app
```

> __Note:__ This app is launched by cron with a `@reboot` macro located inside of the system crontab.
