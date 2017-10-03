export const state = () => ({
  loading: true
})

export const mutations = {
  toggleLoading (state) {
    state.loading = !state.loading
  }
}
