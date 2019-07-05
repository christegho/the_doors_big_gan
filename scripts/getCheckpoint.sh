i=5
rm D.pth D_optim.pth G.pth G_ema.pth G_optim.pth state_dict.pth
cp D_copy${i}.pth D.pth
cp D_optim_copy${i}.pth D_optim.pth
cp G_copy${i}.pth G.pth
cp G_ema_copy${i}.pth G_ema.pth
cp G_optim_copy${i}.pth G_optim.pth
cp state_dict_copy${i}.pth state_dict.pth