<template>
  <n-grid cols="2 s:2 m:2 l:3 xl:3 2xl:3" responsive="screen">
    <n-grid-item>
      <n-form :label-width="80" :model="formValue" :rules="rules" ref="formRef">
        <n-form-item label="昵称" path="name">
          <n-input v-model:value="formValue.name" placeholder="请输入昵称" />
        </n-form-item>

        <n-form-item label="邮箱" path="email">
          <n-input placeholder="请输入邮箱" v-model:value="formValue.email" />
        </n-form-item>

        <n-form-item label="联系电话" path="mobile">
          <n-input placeholder="请输入联系电话" v-model:value="formValue.mobile" />
        </n-form-item>

        <n-form-item label="联系地址" path="address">
          <n-input v-model:value="formValue.address" type="textarea" placeholder="请输入联系地址" />
        </n-form-item>

        <div>
          <n-space>
            <n-button type="primary" @click="formSubmit">更新基本信息</n-button>
          </n-space>
        </div>
      </n-form>
    </n-grid-item>
  </n-grid>
</template>

<script lang="ts">
import { defineComponent, ref, reactive } from 'vue';
import { useMessage } from 'naive-ui';

export default defineComponent({
  setup() {
    const formRef = ref<any>(null);
    const message = useMessage();

    const formValue = reactive({
      name: '',
      mobile: '',
      email: '',
      address: '',
    });

    const rules = {
      name: [{ required: true, message: '请输入昵称', trigger: 'blur' }],
      email: [{ required: true, message: '请输入邮箱', trigger: 'blur' }],
      mobile: [{ required: true, message: '请输入联系电话', trigger: 'input' }],
    };

    const formSubmit = () => {
      formRef.value.validate((errors: any) => {
        if (!errors) {
          message.success('验证成功');
        } else {
          message.error('验证失败，请填写完整信息');
        }
      });
    };

    return {
      formValue,
      rules,
      formSubmit,
    };
  },
});
</script>
