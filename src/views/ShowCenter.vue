<template>
  <h3>天气查询</h3>

  <a-row>
    <a-col :span="8" :offset="6">
      <a-input-search
        v-model:value="adcode"
        placeholder="城市编码  默认唐山"
        enter-button="搜索"
        size="large"
        @search="fetchWeatherData"
      />
    </a-col>
  </a-row>
  <a-col :span="16" :offset="3">
    <a-table
      :columns="columns"
      :row-key="record => record.adcode"
      :data-source="dataSource"
      :pagination="pagination"
      :loading="loading"
      @change="handleTableChange"
    >
      <template #bodyCell="{ column, text }">
        <template v-if="column.dataIndex === 'city'">{{ text }}</template>
        <template v-else-if="column.dataIndex === 'weather'">{{ text }}</template>
        <template v-else-if="column.dataIndex === 'temperature'">{{ text }}°C</template>
        <template v-else-if="column.dataIndex === 'humidity'">{{ text }}%</template>
        <template v-else-if="column.dataIndex === 'winddirection'">{{ text }}</template>
        <template v-else-if="column.dataIndex === 'windpower'">{{ text }}</template>
      </template>
    </a-table>
  </a-col>
</template>

<script lang="ts" setup>
import { ref, computed, onMounted } from 'vue';
import type { TableProps } from 'ant-design-vue';
import axios from 'axios';

const columns = [
  {
    title: 'City',
    dataIndex: 'city',
    key: 'city',
  },
  {
    title: 'Weather',
    dataIndex: 'weather',
    key: 'weather',
  },
  {
    title: 'Temperature (°C)',
    dataIndex: 'temperature',
    key: 'temperature',
  },
  {
    title: 'Humidity (%)',
    dataIndex: 'humidity',
    key: 'humidity',
  },
  {
    title: 'Wind Direction',
    dataIndex: 'winddirection',
    key: 'winddirection',
  },
  {
    title: 'Wind Power',
    dataIndex: 'windpower',
    key: 'windpower',
  },
];

interface WeatherData {
  adcode: string;
  city: string;
  weather: string;
  temperature: string;
  humidity: string;
  winddirection: string;
  windpower: string;
}

const dataSource = ref<WeatherData[]>([]);
const loading = ref(false);
const adcode = ref('130200'); // 默认城市编码为唐山

const pagination = computed(() => ({
  total: dataSource.value.length,
  current: 1,
  pageSize: dataSource.value.length,
}));

const fetchWeatherData = async () => {
  if (!adcode.value) return;

  loading.value = true;
  try {
    const apiUrl = `https://restapi.amap.com/v3/weather/weatherInfo?city=${adcode.value}&key=4cf703d58f4aeeeed5d3b2cb09b01220`;
    const response = await axios.get(apiUrl);
    if (response.data && response.data.lives && response.data.lives.length > 0) {
      const weatherInfo = response.data.lives[0];
      dataSource.value = [
        {
          adcode: weatherInfo.adcode,
          city: weatherInfo.city,
          weather: weatherInfo.weather,
          temperature: weatherInfo.temperature,
          humidity: weatherInfo.humidity,
          winddirection: weatherInfo.winddirection,
          windpower: weatherInfo.windpower,
        },
      ];
    } else {
      dataSource.value = [];
    }
  } catch (error) {
    console.error('请求天气数据时出错:', error);
  } finally {
    loading.value = false;
  }
};

const handleTableChange: TableProps['onChange'] = () => {
  fetchWeatherData();
};

onMounted(() => {
  fetchWeatherData();
});
</script>

<style scoped>
/* 你的样式代码 */
</style>
