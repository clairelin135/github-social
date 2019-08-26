class Routes {
  get user() {
    return {
      show: (username) => `/api/user/${username}`,
    }
  }
  get events() {
    return {
      user_events: (username) => `/api/events/${username}`,
      like: (id) => `/api/events/${id}`,
    }
  }
}
const RoutesAPI = new Routes();
export default RoutesAPI;
