<template>
  <main>
    <router-link to="chart2">to second subpage </router-link>
    <g2-pie
      :type="'pie'"
      :axis-name="{name:'年份', value:'GDP(亿美元)'}"
      :data="chart_data"
      :label-option="{show:true, offset: 20}"
    ></g2-pie>
    <section>
        <button @click="postdata"> save </button> 
    </section>
  </main>
</template>

<script>
import { setInterval } from 'timers';
// data="[{ name: '2016', value: 2 },{ name: '2017', value: 1 },{ name: '2018', value: 3 }]"
export default {
  data() {
    return {
      chart_data: [],
      loop: undefined,
    };
  },
  mounted() {
      this.fetchCharts()
      this.loop = setInterval(()=>this.fetchCharts(), 125 << 8)
  },
  methods: {
    fetchCharts() {
     // Omit error handling
      this.axios.get("chart").then(res => {
        let { data } = res.data;
        // .. 
        let _chart_data = [...data.charts]
        _chart_data.push({
          name: "1999",
          value: Math.round(Math.random() * 10) + 10
        });
        this.chart_data = _chart_data;
      });
    },
    postdata () {
        this.axios.post('chart', this.chart_data[0])
    }
  },
  beforeDestroy() {
    //   this.loop = null
  }
};
</script>

<style scoped >
    section {
        text-align: center
    }
        button {
            font-size: 30px;
        }
</style>

