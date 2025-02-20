/* ---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *-------------------------------------------------------------------------------------------- */
import * as path from 'path';
import { PathConstants, AzConfiguration, CodeGenConstants } from '../../utils/models';
import { thoughtAsTrue } from '../../utils/helper';
import { GeneratorBase } from './Base';
import { CodeModelAz } from '../codemodel/CodeModelAz';
import { GenerateNamespaceInit } from '../renders/CliNamespaceInit';
import { CliTopAction } from '../renders/CliTopAction';
import { CliTopCustom } from '../renders/CliTopCustom';
import { CliReport } from '../renders/CliReport';
import { CliTopInit } from '../renders/CliTopInit';
import { CliTopMetadata } from '../renders/extraExt/CliExtMetadata';
import { CliExtSetupPy } from '../renders/extraExt/CliExtSetupPy';
import { CliActions } from '../renders/generated/CliActions';
import { GenerateAzureCliClientFactory } from '../renders/generated/CliClientFactory';
import { CliCommands } from '../renders/generated/CliCommands';
import { GenerateAzureCliCustom } from '../renders/generated/CliCustom';
import { GenerateAzureCliHelp } from '../renders/generated/CliHelp';
import { GenerateAzureCliParams } from '../renders/generated/CliParams';
import { GenerateAzureCliValidators } from '../renders/generated/CliValidators';
import { CliTestInit } from '../renders/tests/CliTestInit';
import { CliTestPrepare } from '../renders/tests/CliTestPrepare';
import { CliTestScenario } from '../renders/tests/CliTestScenario';
import { CliTestStep, NeedPreparers } from '../renders/tests/CliTestStep';
import { GenerateMetaFile } from '../renders/CliMeta';
import { CliExtSetupCfg } from '../renders/extraExt/CliExtSetupCfg';
import { CliExtHistory } from '../renders/extraExt/CliExtHistory';
import { CliExtReadme } from '../renders/extraExt/CliExtReadme';
import { CliCmdletTest } from '../renders/tests/CliTestCmdlet';
import { SimpleTemplate } from '../renders/TemplateBase';
import { CliTopHelp } from '../renders/CliTopHelp';

export class AzExtensionFullGenerator extends GeneratorBase {
    constructor(model: CodeModelAz) {
        super(model);
        const { configHandler } = model.GetHandler();
        this.azDirectory = configHandler.AzextFolder;
    }

    public async generateAll(): Promise<void> {
        const { extensionHandler, configHandler, exampleHandler } = this.model.GetHandler();
        this.files[path.join(this.azDirectory, 'generated/_params.py')] = GenerateAzureCliParams(
            this.model,
            this.isDebugMode,
        );
        this.files[path.join(this.azDirectory, 'generated/custom.py')] = GenerateAzureCliCustom(
            this.model,
        );
        this.files[
            path.join(this.azDirectory, 'generated/_client_factory.py')
        ] = GenerateAzureCliClientFactory(this.model);
        this.files[
            path.join(this.azDirectory, 'generated/_validators.py')
        ] = GenerateAzureCliValidators(this.model);
        this.files[path.join(this.azDirectory, 'generated/__init__.py')] = GenerateNamespaceInit(
            this.model,
        );
        this.files[path.join(this.azDirectory, 'tests/latest/__init__.py')] = GenerateNamespaceInit(
            this.model,
        );

        this.files[path.join(this.azDirectory, 'generated/_help.py')] = GenerateAzureCliHelp(
            this.model,
            this.isDebugMode,
        );

        this.files[path.join(this.azDirectory, 'manual/__init__.py')] = GenerateNamespaceInit(
            this.model,
        );

        if (configHandler.SDK_NeedSDK) {
            this.files[
                path.join(this.azDirectory, 'vendored_sdks/__init__.py')
            ] = GenerateNamespaceInit(this.model);
        }

        await this.generateFullSingleAndAddtoOutput(new CliActions(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliCommands(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliTopAction(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliTopCustom(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliTopInit(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliTopHelp(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliTopMetadata(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliReport(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliExtHistory(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliExtReadme(this.model), false);
        await this.generateFullSingleAndAddtoOutput(new CliExtSetupCfg(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliExtSetupPy(this.model));

        await this.generateFullSingleAndAddtoOutput(new CliTestInit(this.model));
        await this.generateFullSingleAndAddtoOutput(new CliTestStep(this.model), true, true);
        const hasTestResourceScenario = this.model.GetHandler().exampleHandler.GetResourcePool()
            .hasTestResourceScenario;
        for (const testGroup of exampleHandler.Example_TestScenario
            ? Object.getOwnPropertyNames(exampleHandler.Example_TestScenario)
            : []) {
            await this.generateFullSingleAndAddtoOutput(
                new CliTestScenario(
                    this.model,
                    hasTestResourceScenario
                        ? PathConstants.testSwaggerScenarioFile(testGroup)
                        : PathConstants.fullTestSceanrioFile(testGroup),
                    exampleHandler.Example_TestScenario[testGroup],
                    testGroup,
                ),
                true,
                true,
            );
        }
        const needPreparers = NeedPreparers();
        if (needPreparers.size > 0) {
            await this.generateFullSingleAndAddtoOutput(
                new CliTestPrepare(this.model, [...needPreparers]),
                true,
                true,
            );
        }
        exampleHandler
            .GetResourcePool()
            .generateArmTemplate(
                this.files,
                path.join(this.azDirectory, PathConstants.testFolder, PathConstants.latestFolder),
            );
        GenerateMetaFile(this.model);
        if (thoughtAsTrue(AzConfiguration.getValue(CodeGenConstants.genCmdletTest, false))) {
            for (const boolVal of [false, true]) {
                await this.generateFullSingleAndAddtoOutput(
                    new CliCmdletTest(this.model, boolVal),
                    true,
                    true,
                );
            }
            await this.generateFullSingleAndAddtoOutput(
                new SimpleTemplate(
                    this.model,
                    path.join(
                        configHandler.AzextFolder,
                        PathConstants.testFolder,
                        PathConstants.cmdletFolder,
                        PathConstants.conftestFile,
                    ),
                    path.join(
                        PathConstants.templateRootFolder,
                        PathConstants.testFolder,
                        PathConstants.cmdletFolder,
                        PathConstants.conftestFile + PathConstants.njkFileExtension,
                    ),
                ),
            );
        }
    }
}
