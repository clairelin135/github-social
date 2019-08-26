import React, { Component } from 'react';
import RoutesAPI from '../helpers/routesAPI';
import axios from 'axios';
import update from 'immutability-helper';

/**
 * @prop id: Integer representing the user ID
 */
export default class UserEvents extends Component {
  constructor(props) {
    super(props);
    this.state = {
      events: [],
      componentDidMount: false,
    };
  }

  componentDidMount() {
    const { username } = this.props.match.params;
    const user_route = RoutesAPI.user.show(username);
    const events_route = RoutesAPI.events.user_events(username);
    axios.all([
      axios.get(user_route),
      axios.get(events_route)
    ]).then(
      response => {
        const [user_response, events_response] = response;
        this.setState({
          user: user_response.data,
          events: events_response.data,
          componentDidMount: true,
        });
      },
      error => {
        console.error(error);
      }
    );
  }

  eventToStr = (event) => {
    let eventStr = event.replace( /([A-Z])/g, " $1" );
    return eventStr.slice(0, eventStr.length - 6);
  }

  getDate = (created_at) => {
    const date = new Date(created_at);
    return date.toDateString();
  }

  like = (id, i) => {
    const like_route = RoutesAPI.events.like(id);
    const payload = {
      num_likes: this.state.events[i].num_likes + 1,
    }
    axios.put(like_route, payload).then(
      response => {
        const newState = update(this.state, {
          events: {
            [i]: {
              num_likes: {
                $apply: function(x) {return x+1;}
              }
            }
          }
        });
        this.setState(newState);
      },
      error => {
        console.error(error);
      }
    );
  }

  render() {
    if (!this.state.componentDidMount) {
      return (
        <div>Loading</div>
      );
    }
    return (
      <div className="center mw8">
        <div className="fl w-30">
          <div className="bg-white pa3">
            <img src={this.state.user.avatar_url} className="mb3"/>
            <div className="mb2">
              <h3>{this.state.user.name}</h3>
              <h4>{this.state.user.login}</h4>
            </div>
            <p>{this.state.user.bio}</p>
          </div>
        </div>
        <div className="fl w-70 pl3">
          {
            this.state.events.map((event, i) => {
              return (
                <div key={event.id} className="bg-white pa3 mb3">
                  <div className="flexcol">
                    <div className="flexrow flex-start">
                      <img src={this.state.user.avatar_url} className="profile-image mr3"/>
                      <div className="flexcol event-header">
                        <div className="flexrow space-between">
                          <h4>{event.actor.display_login}</h4>
                          <div className="flexrow flexstart">
                            <p className="i silver mr3">{this.getDate(event.created_at)}</p>
                            <div className="bg-light-gray pv1 ph2 ttl">
                              <p className="code">{this.eventToStr(event.type)}</p>
                            </div>
                          </div>
                        </div>
                        <p>Contributed to <span className="code bg-light-gray pv1 ph2">{event.repo.name}</span></p>
                      </div>
                    </div>
                    <div className="mt3">
                      <div className="flexrow flex-start">
                        <div className="button white bg-dark-gray pv1 ph2 br4 mr3" onClick={() => {this.like(event.id, i)}}>
                          <p>{'\u2665'}</p>
                        </div>
                        <p>Liked by {event.num_likes} people</p>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })
          }
        </div>
      </div>
    );
  }
}
