<template>
  <div class="release">
    <div class="search">
      <a-row>
        <a-col :span="8">
          <a-form-item :label-col="formItemLayout.labelCol" :wrapper-col="formItemLayout.wrapperCol" label="环境名称：">
            <a-input v-model:value="searchKeyword" placeholder="请输入"/>
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
      <a-table :columns="columns" :dataSource="data" rowKey="id">
        <template #action="{ text, record }">
          <router-link to="/">编辑</router-link>
          <span style="color: lightgray"> | </span>
          <router-link to="/">删除</router-link>
        </template>
      </a-table>
    </div>
    <div>
      <a-modal width="720px" v-model:visible="visible" title="新建环境" @ok="handleOk">
        <a-form :model="formState" :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }" @submit="handleSubmit" ref="form">
          <a-form-item label="环境名称" :rules="[ { required: true, message: '请输入环境名称' } ]">
            <a-input v-model:value="formState.name"/>
          </a-form-item>
          <a-form-item label="唯一标识符" :rules="[ { required: true, message: '请输入唯一标识符' } ]">
            <a-input v-model:value="formState.tag"/>
          </a-form-item>
          <a-form-item label="备注信息">
            <a-input v-model:value="formState.description" type="textarea"/>
          </a-form-item>
        </a-form>
      </a-modal>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';
import { Form, Row, Col, Input, Button, Table, Modal, message } from 'ant-design-vue';
import axios from 'axios';

const columns = [
  { title: '序号', dataIndex: 'id', key: 'id' },
  { title: '环境名称', dataIndex: 'name', key: 'name' },
  { title: '标识符', dataIndex: 'tag', key: 'tag' },
  { title: '描述信息', dataIndex: 'description', key: 'description' },
  { title: '操作', dataIndex: '', key: 'x', slots: { customRender: 'action' } },
];

const formItemLayout = {
  labelCol: { span: 5 },
  wrapperCol: { span: 12 },
};

const formState = reactive({
  name: '',
  tag: '',
  description: ''
});

let data = reactive([]);

let visible = false;

const getEnvironmentsData = () => {
  let token = sessionStorage.token || localStorage.token;
  axios.get(`${import.meta.env.VITE_APP_API_HOST}/conf_center/environment`, {
    headers: {
      Authorization: 'jwt ' + token,
    }
  })
  .then((res) => {
    data = res.data;
  })
  .catch((error) => {
    console.error(error);
  });
};

const handleSubmit = (e) => {
  e.preventDefault();
  refs.form.validate().then((values) => {
    let token = sessionStorage.token || localStorage.token;
    axios.post(`${import.meta.env.VITE_APP_API_HOST}/conf_center/environment`, values, {
      headers: {
        Authorization: 'jwt ' + token,
      }
    })
    .then((res) => {
      message.success('添加成功！');
      data.push(res.data);
      visible = false;
    })
    .catch((error) => {
      console.error(error);
    });
  });
};

const showModal = () => {
  visible = true;
};

const handleOk = (e) => {
  handleSubmit(e);
};
</script>

<style scoped>

</style>
