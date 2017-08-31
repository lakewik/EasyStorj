<div class="row sameheight-container">
                            <div class="col-xl-12">

     <div class="card sameheight-item items" data-exclude="xs,sm,lg">
                                    <div class="card-header bordered">
                                        <div class="header-block">
                                            <h3 class="title"> Your playlists </h3>&nbsp;&nbsp;<a style="color: white;" onclick="open_playlist_add_window();" class="btn btn-primary btn-sm rounded">
            				+ Add new playlist
            			</a> </div>
                                        <div class="header-block pull-right">

                                        </div>
                                    </div>
                                    <ul class="item-list striped">
                                        <li class="item item-list-header hidden-sm-down">
                                            <div class="item-row">
                                                <div class="item-col item-col-header fixed item-col-img xs">#</div>
                                                <div class="item-col item-col-header item-col-title">
                                                    <div> <span>Name</span> </div>
                                                </div>
                                                <div class="item-col item-col-header item-col-sales">
                                                    <div> <span>Category</span> </div>
                                                </div>
                                                 <div class="item-col item-col-header item-col-stats">
                                                    <div class="no-overflow"> <span>Tracks count</span> </div>
                                                </div>
                                                <div class="item-col item-col-header item-col-stats">
                                                    <div class="no-overflow"> <span>Description</span> </div>
                                                </div>
                                                 <div class="item-col item-col-header item-col-date">
                                                    <div> <span>...</span> </div>
                                                </div>
                                            </div>
                                        </li>
                                         {% set i = [0] %}
                                         {% for playlist in playlists_array %}
                                         {% if i.append(i.pop() + 1) %}{% endif %}

                                        <li class="item">
                                            <div class="item-row">
                                                <div class="item-col fixed item-col-img xs">
                                                   {{ i[0] }}

                                                </div>
                                                <div class="item-col item-col-title no-overflow">
                                                    <div>
                                                        <a href="/playlist_tracks_manager\{{ playlist.eid }}" class="">
                                                            <h4 class="item-title no-wrap"> {{ playlist["name"] }} </h4>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="item-col item-col-sales">
                                                    <div class="item-heading">Category</div>
                                                    <div> {{ playlist["category"] }} </div>
                                                </div>
                                                <div class="item-col item-col-sales">
                                                    <div class="item-heading">Tracks count</div>
                                                    <div> {{ playlist_tracks_count[i[0]-1] }} </div>
                                                </div>
                                                <div class="item-col item-col-date">
                                                    <div class="item-heading">Created</div>
                                                    <div> </div>
                                                </div>
                                                <div class="item-col">
                                                    <div class="item-heading">Options</div>
                                                    <div> <a href="item-editor.html" class="btn btn-primary btn-sm rounded" style="width: 23%;"><em class="fa fa-upload"></em></a>

            			                                                      <a href="/playlist_tracks_manager/{{ playlist.eid }}" class="btn btn-warning btn-sm rounded" style="width: 24%;">
            				<em class="fa fa-list"></em></a>

                                                          <a href="item-editor.html" class="btn btn-info btn-sm rounded" style="width: 23%;">
            				<em class="fa fa-sign-out"></em>
            			</a>

                                                             <a href="#" onclick="delete_playlist(`{{ playlist.eid }}`, `{{ playlist['name'] }}` );" class="btn btn-danger btn-sm rounded" style="width: 24%;">
            				<em class="fa fa-times"></em>
            			</a> </div>
                                                </div>
                                            </div>
                                        </li>

                                        {% endfor %}
                                    </ul>
                                </div>

    </div>

                        </div>
