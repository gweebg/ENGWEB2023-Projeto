
<script>

    import { beforeNavigate } from "$app/navigation";
    import { page } from "$app/stores";
    import { enhance } from "$app/forms";
    import { fade } from "svelte/transition";

    import { initFlash } from "sveltekit-flash-message/client";
    import { superForm } from 'sveltekit-superforms/client';

    import {switchPassword} from "$lib/scripts/passwordInputState.js";
	import { PUBLIC_GOOGLE_CLIENT_ID } from "$env/static/public";

    export let data;

    const { form, errors } = superForm(data.form);
    const flash = initFlash(page);

    let alert = true;
    let buttonContent = "Entrar";
    let loading = false;


    const submitHandler = () => {

        loading = true;
        buttonContent = "A entrar..."

        return async ({ update}) => {
            await update();
            loading = false;
            buttonContent = "Entrar"
        }

    }

    beforeNavigate((nav) => {
        if ($flash && nav.from?.url.toString() !== nav.to?.url.toString()) {
            $flash = undefined;
        }
    });


</script>

<svelte:head>
    <script src="https://accounts.google.com/gsi/client" async defer></script>
    <title>
        Acordb - Entrar
    </title>
</svelte:head>

<div class="flex justify-center items-center h-screen flex-col">

    <!-- Flash Message Alert -->
    {#if $flash && $flash.message && alert}

        <div class="alert alert-warning w-1/3 mb-4" transition:fade>
            <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <span>{$flash.message}</span>
            <button class="ml-auto btn btn-sm btn-ghost btn-circle" on:click={() => alert = false}>×</button>
        </div>

    {/if}

    <div class="card w-1/3 shadow-xl bg-white">

        <!-- Card Header (Logo) -->
        <div class="flex justify-center">
            <a href="/home">
                <img class="w-40 h-30 pt-4" src="logo-textless.svg" alt="logo"/>
            </a>
        </div>

        <!-- Card Body (Title, Form, Sign In Button, Continue With)-->
        <div class="card-body">

            <!-- Title -->
            <h1 class="text-text_base text-center gap-2 text-3xl font-semibold leading-7">Entrar em Acordb</h1>

            <!-- Card Body and Form -->
            <form method="POST" class="pt-4" use:enhance={submitHandler}>

                <label class="label" for="email">
                    <span class="label-text">Insira o email</span>
                </label>
                <input
                        id="email"
                        name="email"
                        type="text"
                        placeholder="Email"
                        class="input input-bordered w-full"
                        disabled={loading}
                        bind:value={$form.email}/>

                {#if $errors.email}
                    <small class="text-error">{$errors.email}</small>
                {/if}

                <!-- Password -->
                <label for="password" class="label pt-4">
                    <span class="label-text">Insira a password</span>
                </label>
                <div class="form-control">
                    <div class="input-group">
                        <input id="password"
                               name="password"
                               type="password"
                               placeholder="Password"
                               class="input input-bordered w-full"
                               disabled={loading}
                        />

                        <button id="passwordIconBtn" type="button" class="btn btn-square btn-secondary" on:click={switchPassword}>
                            <img id="passwordIcon" src="/icons/profile/eye-closed.svg" alt="Eye">
                        </button>

                    </div>
                </div>
                {#if $errors.password}
                    <small class="text-error">{$errors.password}</small>
                {/if}

                <label class="label cursor-pointer pt-6 justify-start" for="remember">
                    <input id="remember" name="remember" type="checkbox" class="checkbox checkbox-primary checkbox-sm mr-2" />
                    <span class="text-md">Lembrar-se de mim</span>
                </label>
                {#if $errors.general}
                    <small class="text-error">{$errors.general}</small>
                {/if}

                <div class="pt-4">
                    <button class="btn btn-primary w-full" disabled={loading}>{buttonContent}</button>
                </div>

            </form>

            <!-- Want to sign up ? -->
            <p class="pt-2 text-gray-500 text-md">
                Não tem uma conta? <a href="/register" class="text-secondary">Registe-se</a>
            </p>

            <div class="flex justify-center">
                <div id="g_id_onload"
                     data-client_id="{PUBLIC_GOOGLE_CLIENT_ID}"
                     data-ux_mode="redirect"
                     data-login_uri="http://localhost/api/login/google">
                </div>
                <div class="g_id_signin" data-type="standard"></div>
            </div>

        </div>
    </div>
</div>