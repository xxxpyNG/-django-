<template>
  <div class="alarm">
    <h2>报警历史</h2>
    <ul>
      <li v-for="history in alarmHistory" :key="history.id">
        {{ history.timestamp }} - {{ history.message }}
      </li>
    </ul>

    <h2>报警联系人</h2>
    <ul>
      <li v-for="contact in alarmContacts" :key="contact.id">
        {{ contact.name }} - {{ contact.email }}
      </li>
    </ul>

    <h2>报警联系组</h2>
    <ul>
      <li v-for="group in alarmGroups" :key="group.id">
        {{ group.name }}
        <ul>
          <li v-for="contact in group.contacts" :key="contact.id">
            {{ contact.name }} - {{ contact.email }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      alarmHistory: [],
      alarmContacts: [],
      alarmGroups: [],
    };
  },
  created() {
    this.fetchAlarmHistory();
    this.fetchAlarmContacts();
    this.fetchAlarmGroups();
  },
  methods: {
    fetchAlarmHistory() {
      axios.get('/api/alarm-history/')
        .then(response => {
          this.alarmHistory = response.data;
        })
        .catch(error => {
          console.error('Error fetching alarm history:', error);
        });
    },
    fetchAlarmContacts() {
      axios.get('/api/alarm-contacts/')
        .then(response => {
          this.alarmContacts = response.data;
        })
        .catch(error => {
          console.error('Error fetching alarm contacts:', error);
        });
    },
    fetchAlarmGroups() {
      axios.get('/api/alarm-groups/')
        .then(response => {
          this.alarmGroups = response.data;
        })
        .catch(error => {
          console.error('Error fetching alarm groups:', error);
        });
    },
  },
};
</script>

<style>
/* Add your styles here */
</style>