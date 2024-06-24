<template>
  <div class="release">
    <div class="search">
      <a-row>
        <a-col :span="8">
          <a-form-item :label-col="formItemLayout.labelCol" :wrapper-col="formItemLayout.wrapperCol" label="环境名称：">
            <a-input v-model="searchName" placeholder="请输入"/>
          </a-form-item>
        </a-col>
        <a-col :span="8">
          <router-link to="/release">
            <a-button type="primary" icon="" style="margin-top: 3px;">刷新</a-button>
          </router-link>
        </a-col>
      </a-row>
    </div>
    <div>
      <a-button type="primary" @click="showModal"><a-icon type="plus"/>新建</a-button>
    </div>
    <div class="app_list">
      <a-table :columns="columns" :data-source="data" rowKey="id">
        <template #action="{ text, record }">
          <router-link to="/">编辑</router-link>
          <span style="color: lightgray"> | </span>
          <router-link to="/">删除</router-link>
        </template>
      </a-table>
    </div>
    <div>
      <a-modal width="720px" v-model:visible="visible" title="新建环境" @ok="handleOk">
        <a-form :model="form" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }" @submit="handleSubmit">
          <a-form-item label="环境名称">
            <a-input v-model="form.name" :rules="[{ required: true, message: '请输入环境名称' }]"/>
          </a-form-item>
          <a-form-item label="唯一标识符">
            <a-input v-model="form.tag" :rules="[{ required: true, message: '请输入唯一标识符' }]"/>
          </a-form-item>
          <a-form-item label="备注信息">
            <a-textarea v-model="form.description"/>
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
  setup() {
    const router = useRouter();

    const formItemLayout = {
      labelCol: { span: 8 },
      wrapperCol: { span: 12 },
    };

    const columns = [
      { title: '序号', dataIndex: 'id', key: 'id' },
      { title: '环境名称', dataIndex: 'name', key: 'name' },
      { title: '标识符', dataIndex: 'tag', key: 'tag' },
      { title: '描述信息', dataIndex: 'description', key: 'description' },
      { title: '操作', dataIndex: '', key: 'x', customRender: 'action' },
    ];

    const searchName = ref('');
    const form = reactive({
      name: '',
      tag: '',
      description: '',
    });

    const data = ref([]);
    const visible = ref(false);

    const getEnvironmentsData = () => {
      const token = sessionStorage.token || localStorage.token;
      axios.get('/conf_center/environment', {
        headers: {
          Authorization: 'jwt ' + token,
        },
      }).then((res) => {
        data.value = res.data;
      }).catch((error) => {
        console.error(error);
      });
    };

    const handleSubmit = (e) => {
      e.preventDefault();
      // Assume form validation passes
      const token = sessionStorage.token || localStorage.token;
      axios.post('/conf_center/environment', form, {
        headers: {
          Authorization: 'jwt ' + token,
        },
      }).then((res) => {
        data.value.push(res.data);
        visible.value = false;
      }).catch((error) => {
        console.error(error);
      });
    };

    const handleOk = (e) => {
      handleSubmit(e);
    };

    const showModal = () => {
      visible.value = true;
    };

    onMounted(() => {
      getEnvironmentsData();
    });

    return {
      formItemLayout,
      columns,
      searchName,
      form,
      data,
      visible,
      getEnvironmentsData,
      handleSubmit,
      handleOk,
      showModal,
    };
  },
};
</script>

<style scoped>
.xx_title:after {
  border: none;
}
</style>
