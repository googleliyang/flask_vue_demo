<template>
  <main>
    <router-link to="chart1">back</router-link>
    <g2-pie
      :type="'pie'"
      :axis-name="{name:'年份', value:'GDP(亿美元)'}"
      :data="chart_data"
      :label-option="{show:true, offset: 20}"
    ></g2-pie>
  </main>
</template>

<script>
export default {
  data() {
    return {
      chart_data: [],
    };
  },
  mounted() {
    this.fetchCharts();
  },
  methods: {
    fetchCharts() {
      // Omit error handling
      this.axios.get("chart2").then(res => {
        let { data } = res.data;
        this.chart_data = data.charts;
      });
    },
  },
};
</script>

<style scoped>
section {
  text-align: center;
}
button {
  font-size: 30px;
}
</style>

