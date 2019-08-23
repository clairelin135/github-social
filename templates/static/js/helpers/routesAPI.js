class RoutesAPI {
  get works() {
    return {
      index: `/api/works`,
      create: `/api/works`,
      show: (id) => `/api/works/${id}`,
      update: (id) => `/api/works/${id}`,
      delete: (id) => `/api/works/${id}`,
      filtered_works: (search_params) => `/api/works/filtered_works/${search_params}`,
      categories: `/works/categories`,
      thumbnail: (id) => `api/works/thumbnail/${id}`
    }
  }
}
const routesAPI = new RoutesAPI();
