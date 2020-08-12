<!DOCTYPE html>
<!-- saved from url=(0026)http://localhost:8888/tree -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>Home</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon.ico?v=97c6417ed01bdc0ae3ef32ae4894fd03">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./Detect_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./Detect_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    <link rel="stylesheet" href="./Detect_files/style.min.css" type="text/css">
    
    <link rel="stylesheet" href="./Detect_files/custom.css" type="text/css">
    <script src="./Detect_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./Detect_files/index.js.download" type="text/javascript"></script>
    <script src="./Detect_files/index.js(1).download" type="text/javascript"></script>
    <script src="./Detect_files/index.js(2).download" type="text/javascript"></script>
    <script src="./Detect_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20200812162402",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./Detect_files/contents.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./Detect_files/custom.js.download"></script></head>

<body class="" data-jupyter-api-token="fd184961d10cc14ac0cd49e190db4698c5d7ba70355f249f" data-base-url="/" data-notebook-path="" data-terminals-available="True" data-server-root="C:\Users\indhu" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=fd184961d10cc14ac0cd49e190db4698c5d7ba70355f249f" title="dashboard">
      <img src="./Detect_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  
  <span class="flex-spacer"></span>
  
    <span id="shutdown_widget">
      <button id="shutdown" class="btn btn-sm navbar-btn" title="Stop the Jupyter server">
          Quit
      </button>
    </span>
  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
  
</div>

<div id="site" style="display: block; height: 535px;">


  <div id="ipython-main-app" class="container">
    <div id="tab_content" class="tabbable">
      <ul id="tabs" class="nav nav-tabs">
        <li class="active"><a href="http://localhost:8888/tree#notebooks" data-toggle="tab">Files</a></li>
        <li><a href="http://localhost:8888/tree#running" data-toggle="tab">Running</a></li>
        <li><a href="http://localhost:8888/tree#clusters" data-toggle="tab" class="clusters_tab_link">Clusters</a></li>
      </ul>
      <div class="tab-content">
        <div id="notebooks" class="tab-pane active">
          <div id="notebook_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <div class="dynamic-instructions" style="display: none;">
                Select items to perform actions on them.
              </div>
              <div class="dynamic-buttons">
                  <button title="Duplicate selected" aria-label="Duplicate selected" class="duplicate-button btn btn-default btn-xs" style="display: inline-block;">Duplicate</button>
                  <button title="Rename selected" aria-label="Rename selected" class="rename-button btn btn-default btn-xs" style="display: inline-block;">Rename</button>
                  <button title="Move selected" aria-label="Move selected" class="move-button btn btn-default btn-xs" style="display: inline-block;">Move</button>
                  <button title="Download selected" aria-label="Download selected" class="download-button btn btn-default btn-xs" style="display: inline-block;">Download</button>
                  <button title="Shutdown selected notebook(s)" aria-label="Shutdown selected notebook(s)" class="shutdown-button btn btn-default btn-xs btn-warning" style="display: none;">Shutdown</button>
                  <button title="View selected" aria-label="View selected" class="view-button btn btn-default btn-xs" style="display: inline-block;">View</button>
                  <button title="Edit selected" aria-label="Edit selected" class="edit-button btn btn-default btn-xs" style="display: inline-block;">Edit</button>
                  <button title="Delete selected" aria-label="Delete selected" class="delete-button btn btn-default btn-xs btn-danger" style="display: inline-block;"><i class="fa fa-trash"></i></button>
              </div>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <div class="pull-right">
                <form id="alternate_upload" class="alternate_upload">
                  <span id="notebook_list_info" class="toolbar_info">
                  <span class="btn btn-xs btn-default btn-upload">
                  <input title="Click to browse for a file to upload." type="file" name="datafile" class="fileinput" multiple="multiple">
                  Upload
                  </span>
                  </span>
                </form>
                <div id="new-buttons" class="btn-group">
                  <button class="dropdown-toggle btn btn-default btn-xs" id="new-dropdown-button" data-toggle="dropdown">
                  <span>New</span>
                  <span class="caret"></span>
                  </button>
                  <ul id="new-menu" class="dropdown-menu">
                    <li role="presentation" class="dropdown-header" id="notebook-kernels">Notebook:</li><li id="kernel-python3"><a href="http://localhost:8888/tree#" title="Create a new notebook with Python 3">Python 3</a></li>
                    <li role="presentation" class="divider"></li>
                    <li role="presentation" class="dropdown-header">Other:</li>
                    <li role="presentation" id="new-file">
                      <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Text File</a>
                    </li>
                    <li role="presentation" id="new-folder">
                      <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Folder</a>
                    </li>
                    
                    <li role="presentation" id="new-terminal">
                      <a role="menuitem" tabindex="-1" href="http://localhost:8888/tree#">Terminal</a>
                    </li>
                    
                  </ul>
                </div>
                <div class="btn-group">
                    <button id="refresh_notebook_list" title="Refresh notebook list" aria-label="Refresh notebook list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
                </div>
              </div>
            </div>
          </div>
          <div id="notebook_list" class="list_container">
            <div id="notebook_list_header" class="row list_header">
              <div class="btn-group dropdown" id="tree-selector">
                <button title="Select All / None" aria-label="Select All / None" type="button" class="btn btn-default btn-xs" id="button-select-all">
                  <input type="checkbox" class="pull-left tree-selector" id="select-all"><span id="counter-select-all">1</span>
                </button>
                <button title="Select..." class="btn btn-default btn-xs dropdown-toggle" type="button" id="tree-selector-btn" data-toggle="dropdown" aria-expanded="true">
                  <span class="caret"></span>
                  <span class="sr-only">Toggle Dropdown</span>
                </button>
                <ul id="selector-menu" class="dropdown-menu" role="menu" aria-labelledby="tree-selector-btn">
                  <li role="presentation"><a id="select-folders" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Folders"><i class="menu_icon folder_icon icon-fixed-width"></i>&nbsp;Folders</a></li>
                  <li role="presentation"><a id="select-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Notebooks"><i class="menu_icon notebook_icon icon-fixed-width"></i>&nbsp;All Notebooks</a></li>
                  <li role="presentation"><a id="select-running-notebooks" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select Running Notebooks"><i class="menu_icon running_notebook_icon icon-fixed-width"></i>&nbsp;Running</a></li>
                  <li role="presentation"><a id="select-files" role="menuitem" tabindex="-1" href="http://localhost:8888/tree#" title="Select All Files"><i class="menu_icon file_icon icon-fixed-width"></i>&nbsp;Files</a></li>
                </ul>
              </div>
              <div id="project_name">
                <ul class="breadcrumb"><li><a href="http://localhost:8888/tree"><i class="fa fa-folder"></i></a></li><li><a href="http://localhost:8888/tree"></a></li></ul>
              </div>
              <div id="file_size" class="pull-right sort_button">
                  <span class="btn btn-xs btn-default sort-action" id="file-size">
                      File size
                      <i class="fa"></i>
                  </span>
              </div>
              <div id="last_modified" class="pull-right sort_button">
                  <span class="btn btn-xs btn-default sort-action" id="last-modified">
                      Last Modified
                      <i class="fa"></i>
                  </span>
              </div>
              <div id="sort_name" class="pull-right sort_button">
                  <span class="btn btn-xs btn-default sort-action" id="sort-name">
                      Name
                      <i class="fa fa-arrow-down"></i>
                  </span>
              </div>
            </div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/3D%20Objects"><span class="item_name">3D Objects</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Anaconda3"><span class="item_name">Anaconda3</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-06-15 18:00">a year ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Anaconda4"><span class="item_name">Anaconda4</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-07-29 19:41">a year ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/AndroidStudioProjects"><span class="item_name">AndroidStudioProjects</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-12-03 11:03">8 months ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/basic%20code"><span class="item_name">basic code</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-09-07 18:42">a year ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Cisco%20Packet%20Tracer%207.2"><span class="item_name">Cisco Packet Tracer 7.2</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2019-10-15 18:33">10 months ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Contacts"><span class="item_name">Contacts</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Desktop"><span class="item_name">Desktop</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-12 16:24">seconds ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Documents"><span class="item_name">Documents</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-11 08:15">a day ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Downloads"><span class="item_name">Downloads</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-12 15:26">an hour ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Favorites"><span class="item_name">Favorites</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Links"><span class="item_name">Links</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Music"><span class="item_name">Music</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/OneDrive"><span class="item_name">OneDrive</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-01 16:57">11 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Pictures"><span class="item_name">Pictures</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/PycharmProjects"><span class="item_name">PycharmProjects</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-04-17 00:13">4 months ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Saved%20Games"><span class="item_name">Saved Games</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Searches"><span class="item_name">Searches</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Untitled%20Folder"><span class="item_name">Untitled Folder</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-01-27 09:50">7 months ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon folder_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/tree/Videos"><span class="item_name">Videos</span></a><span class="file_size pull-right">&nbsp;</span><span class="item_modified pull-right" title="2020-08-04 09:32">8 days ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon notebook_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/notebooks/Untitled.ipynb" target="_blank"><span class="item_name">Untitled.ipynb</span></a><span class="file_size pull-right">3.05 kB</span><span class="item_modified pull-right" title="2020-08-12 15:15">an hour ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div><div class="list_item row"><div class="col-md-12"><input type="checkbox" title="Click here to rename, delete, etc."><i class="item_icon file_icon icon-fixed-width"></i><a class="item_link" href="http://localhost:8888/edit/Detect.py" target="_blank"><span class="item_name">Detect.py</span></a><span class="file_size pull-right">3.05 kB</span><span class="item_modified pull-right" title="2020-08-12 15:54">30 minutes ago</span><div class="item_buttons pull-right"><div class="running-indicator" style="visibility: hidden;">Running</div></div></div></div>
          </div>
        </div>
        <div id="running" class="tab-pane">
          <div id="running_toolbar" class="row list_toolbar">
            <div class="col-sm-8 no-padding">
              <span id="running_list_info" class="toolbar_info">Currently running Jupyter processes</span>
            </div>
            <div class="col-sm-4 no-padding tree-buttons">
              <span id="running_buttons" class="pull-right toolbar_buttons">
              <button id="refresh_running_list" title="Refresh running list" aria-label="Refresh running list" class="btn btn-default btn-xs"><i class="fa fa-refresh"></i></button>
              </span>
            </div>
          </div>
          <div class="panel-group" id="accordion">
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseOne" href="http://localhost:8888/tree#">
                  Terminals
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseOne" class=" collapse in">
                <div class="panel-body">
                  <div id="terminal_list" class="list_container">
                    <div id="terminal_list_header" class="row list_placeholder">
                    
                      <div> There are no terminals running. </div>
                    
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="panel panel-default">
              <div class="panel-heading">
                <a data-toggle="collapse" data-target="#collapseTwo" href="http://localhost:8888/tree#">
                  Notebooks
                <i class="fa fa-caret-down"></i></a>
              </div>
              <div id="collapseTwo" class=" collapse in">
                <div class="panel-body">
                  <div id="running_list" class="list_container">
                    <div id="running_list_placeholder" class="row list_placeholder">
                      <div> There are no notebooks running. </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="clusters" class="tab-pane">
          Clusters tab is now provided by IPython parallel.
          See '<a href="https://github.com/ipython/ipyparallel">IPython parallel</a>' for installation details.
        </div>
      </div><!-- class:tab-content -->
    </div><!-- id:tab_content -->
  </div><!-- ipython-main-app  -->


</div>





    



<script src="./Detect_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>


<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


</body></html>